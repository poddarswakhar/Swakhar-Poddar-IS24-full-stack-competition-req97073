import React, { Component } from "react";

// Header file

class Header extends Component {
  // if it clicks on the logo the page reloads, for better user experience
  handleDivClick = () => {
    window.location.reload();
  };
  render() {
    return (
      <div className="text-center" >
        <div style={{backgroundColor: '#003366', borderBottom: "4px solid #fcba19" }} onClick={this.handleDivClick}>
            <img
            src="https://www2.gov.bc.ca/StaticWebResources/static/gov3/images/gov_bc_logo.svg"
            width="300"
            className="img-thumbnail"
            style={{ marginTop: "20px", backgroundColor: '#003366', border: "none" }}
            />
            <hr />
        </div>

        <br></br>

        <h5>
          <i>presents</i>
        </h5>
        <h1>IMB Catalog</h1>
        <br></br>
      </div>
    );
  }
}

export default Header;