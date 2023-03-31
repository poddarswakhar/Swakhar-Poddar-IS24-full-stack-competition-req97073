import React, { Component } from "react";
import { Table } from "reactstrap";
import NewProductModal from "./NewProductModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

// This file is the file that displays all the list of the products after doing the query in the Home.js
// also renders the remove confirmation when delete is pressed
// Again the render part is self sufficient to understand, using elements with some inline css

class ProductList extends Component {
  render() {
    const products = this.props.products;
    return (
      <div>
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
                  <b>No Products!</b>
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
                      products={prod}
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
          <br></br>
        </Table>
        <div className="text-center">
          <b>Total Products: {products.length}</b>
        </div>
      </div>
    );
  }
}

export default ProductList;