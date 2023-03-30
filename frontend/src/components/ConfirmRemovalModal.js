import React, { Component, Fragment } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

import { API_URL_D } from "../constants";

class ConfirmRemovalModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  deleteProduct = pk => {
    axios.delete(API_URL_D + "?id=" + pk).then(() => {
      this.props.resetState();
      this.toggle();
    }).catch(error => {
      alert("ERROR: Couldn't Delete the Product! Check the Console Log");
      console.error(error);
      this.props.resetState();
    });
  };

  render() {
    return (
      <Fragment>
        <Button color="danger" onClick={() => this.toggle()}>
          Remove
        </Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>
            Do you really want to delete this product?
          </ModalHeader>

          <ModalFooter>
            <Button type="button" onClick={() => this.toggle()} style = {{backgroundColor: "#385a8a"}}>
              Cancel
            </Button>
            <Button
              type="button"
              color="danger"
              onClick={() => this.deleteProduct(this.props.pk)}
            >
              Yes
            </Button>
          </ModalFooter>
        </Modal>
      </Fragment>
    );
  }
}

export default ConfirmRemovalModal;