import React, { Component } from "react";
import { Table } from "reactstrap";
import NewProductModal from "./NewProductModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class ProductList extends Component {
  render() {
    const products = this.props.products;
    return (
      <Table striped>
        <thead>
          <tr>
            <th>Product Number</th>
            <th>Product Name</th>
            <th>Product Owner</th>
            <th>Developer Name(s)</th>
            <th>Scrum Master</th>
            <th>Start Date</th>
            <th>Methodology</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!products || products.length <= 0 ? (
            <tr>
              <td colSpan="9" align="center">
                <b>No Products Registered Yet! Please Create New</b>
              </td>
            </tr>
          ) : (
            products.map(prod => (
              <tr key={prod.productId}>
                <td>{prod.productId}</td>
                <td>{prod.productName}</td>
                <td>{prod.productOwnerName}</td>
                <td>
                  <tr>{prod.Developers[0]}</tr>
                  <tr>{prod.Developers[1]}</tr>
                  <tr>{prod.Developers[2]}</tr>
                  <tr>{prod.Developers[3]}</tr>
                  <tr>{prod.Developers[4]}</tr>
                </td>
                <td>{prod.scrumMasterName}</td>
                <td>{prod.startDate}</td>
                <td>{prod.methodology}</td>
                <td align="center">
                  <NewProductModal
                    create={false}
                    prod={prod}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={prod.productId}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default ProductList;