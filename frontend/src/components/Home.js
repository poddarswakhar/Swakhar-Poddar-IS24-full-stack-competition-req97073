import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ProductList from "./ProductList";
import NewProductModal from "./NewProductModal";

import axios from "axios";
import { API_URL, API_URL_S, API_URL_H } from "../constants";

class Home extends Component {
  state = {
    products: [],
    searchTerm: "",
    isHealthy: null,
  };

  componentDidMount() {
    this.resetState();
  }

  getProducts = () => {
    axios.get(API_URL).then(res => this.setState({ products: res.data, isHealthy: true }))
    .catch(error => {
      this.health();
    });
  }

  resetState = () => {
    this.setState({ isHealthy: null }, () => {
      // reset products and searchTerm after resetting health status
      this.getProducts();
      this.setState({ searchTerm: "" });
    });
  };

  handleSearchChange = (event) => {
    this.setState({ searchTerm: event.target.value });
  };

  searchProducts = () => {
    axios.get(API_URL_S + `?src=${this.state.searchTerm}`).then((res) => {
      this.setState({ products: res.data, isHealthy: true });
    }).catch(error => {
      this.health();
    });
  };

  health = () => {
    axios.get(API_URL_H).then(response => {
    console.log(response); // should log a 200 OK response
    this.setState({ isHealthy: true });
  })
  .catch(error => {
    console.error(error);
    //alert("Component is not healthy! :(");
    this.setState({ isHealthy: false });
  });
  }

  render() {
    if (this.state.isHealthy === null) {
      return (
        <div className="text-center">
          <h2>Loading . . . ⌛</h2>
        </div>
      );
    }
    else if (!this.state.isHealthy) {
      return (
        <div className="text-center">
          <h1>⚠️</h1>
          <h2>Component is not healthy!</h2>
          <b>Check Running the Backend Server on Port 3000</b>
        </div>
      );
    }
    return (
      <Container style={{ marginTop: "20px" }}>
        <div style={{ paddingLeft: "32%",}}>
        <Row>
            <Col>
                <input
                type="text"
                placeholder="Search Scrum Master or Developer"
                value={this.state.searchTerm}
                onChange={this.handleSearchChange}
                style={{
                    width: "100%",
                    borderRadius: "20px",
                    padding: "10px",
                    boxSizing: "border-box",
                }}
                />
            </Col>
            <Col>   
                <button
                onClick={this.searchProducts}
                style={{
                    marginTop: "0px",
                    borderRadius: "20px",
                    padding: "10px 20px",
                    boxSizing: "border-box",
                    backgroundColor: "#385a8a"
                }}
                >
                <b style={{color: "white"}}>Search</b>
                </button>
            </Col>
        </Row>
        </div>
        <br></br><br></br>
        <Row>
          <Col>
            <ProductList
              products={this.state.products}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewProductModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;