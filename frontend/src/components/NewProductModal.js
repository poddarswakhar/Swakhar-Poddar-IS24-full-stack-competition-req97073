import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewProductForm from "./NewProductForm";

class NewProductModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Editing Product";
    var button = <Button style={{ backgroundColor: "#385a8a" }} onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Creating New Product";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px", backgroundColor: "#385a8a" }}
        >
          Create New
        </Button>
      );
    }

    return (
      <Fragment>
      <br></br>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewProductForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              products={this.props.products}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewProductModal;