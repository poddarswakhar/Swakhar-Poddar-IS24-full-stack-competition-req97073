import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ProductList from "./ProductList";
import NewProductModal from "./NewProductModal";

import axios from "axios";
import { API_URL, API_URL_S, API_URL_H } from "../constants";

// This is the top heirarchy JS file

class Home extends Component {
  // the variable we have to keep track
  state = {
    products: [], // queryset
    searchTerm: "", // for search param
    isHealthy: null, // for healthy backend endpoint check
  };

  // states management
  componentDidMount() {
    this.resetState();
  }

  // using axios to do the GET request for all the product
  getProducts = () => {
    axios.get(API_URL).then(res => this.setState({ products: res.data, isHealthy: true }))
    .catch(error => {
      this.health();
    });
  }

  // reset state method for state management
  resetState = () => {
    this.setState({ isHealthy: null }, () => {
      // reset products and searchTerm after resetting health status
      this.getProducts();
      this.setState({ searchTerm: "" });
    });
  };

  // method for search button action
  handleSearchChange = (event) => {
    this.setState({ searchTerm: event.target.value });
  };

  // using axios to do the GET request with the search param
  searchProducts = () => {
    axios.get(API_URL_S + `?src=${this.state.searchTerm}`).then((res) => {
      this.setState({ products: res.data, isHealthy: true });
    }).catch(error => {
      this.health();
    });
  };

  // method for checking the health state of backend
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

  // rendering the feont end, if the state is not healthy show not healthy message, in the meantime of the request to be made and the state to be updated, show Loading message
  // The other render part is self sufficient to understand, using elements with some inline css
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