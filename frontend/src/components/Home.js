import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ProductList from "./ProductList";
import NewProductModal from "./NewProductModal";

import axios from "axios";
import { API_URL } from "../constants";

class Home extends Component {
  state = {
    products: [],
    searchTerm: "",
  };

  componentDidMount() {
    this.resetState();
  }

  getProducts = () => {
    axios.get(API_URL).then(res => this.setState({ products: res.data }));
  };

  resetState = () => {
    this.getProducts();
    this.setState({ searchTerm: "" });
  };

  handleSearchChange = (event) => {
    this.setState({ searchTerm: event.target.value });
  };

  searchProducts = () => {
    axios.get(API_URL + `?search=${this.state.searchTerm}`).then((res) => {
      this.setState({ products: res.data });
    });
  };

  render() {
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
                    backgroundColor: "#fcba19"
                }}
                >
                <b>Search</b>
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