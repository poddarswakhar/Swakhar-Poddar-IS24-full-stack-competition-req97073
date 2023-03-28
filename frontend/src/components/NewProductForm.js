import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL, API_URL_D } from "../constants";

class NewProductForm extends React.Component {
  state = {
    productId: 0,
    productName: "",
    productOwnerName: "",
    Developers: "",
    scrumMasterName: "",
    startDate: "",
    methodology: ""
  };

  componentDidMount() {
    if (this.props.products) {
      const { productId, productName, productOwnerName, Developers, scrumMasterName, startDate, methodology} = this.props.products;
      this.setState({ productId, productName, productOwnerName, Developers, scrumMasterName, startDate, methodology });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createProduct = e => {
    //this.state["Developers"] = this.state["Developers"].split(",");
    e.preventDefault();
    this.state.Developers = this.state.Developers.toString().split(",");
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    }).catch(error => {
      alert("WARNING: Product is not Created! Check the fields again! Make sure the data is in desired format!");
      console.error(error);
      this.props.resetState();
    });
  };

  editProduct = e => {
    //this.state["Developers"] = this.state["Developers"].split(",");
    e.preventDefault();
    this.state.Developers = this.state.Developers.toString().split(",");
    axios.put(API_URL_D + "?id=" + this.state.productId, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    }).catch(error => {
      alert("WARNING: Product is not Updated! Check the fields again! Make sure the data is in desired format!");
      console.error(error);
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.products ? this.editProduct : this.createProduct}>
        <FormGroup>
          <Label for="productName">Product Name:</Label>
          <Input
            type="text"
            name="productName"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.productName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="productOwnerName">Product Owner:</Label>
          <Input
            type="text"
            name="productOwnerName"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.productOwnerName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Developers">Developers (For multiple use comma):</Label>
          <Input
            type="text"
            name="Developers"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.Developers)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="scrumMasterName">Scrum Master:</Label>
          <Input
            type="text"
            name="scrumMasterName"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.scrumMasterName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="startDate">Start Date (YYYY-MM-DD):</Label>
          <Input
            type="date-input"
            name="startDate"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.startDate)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="methodology">Methodology:</Label>
          <Input
            type="text"
            name="methodology"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>
        <Button style={{ backgroundColor: "#385a8a" }}>Confirm</Button>
      </Form>
    );
  }
}

export default NewProductForm;