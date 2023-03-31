import React, { Component } from "react";

// Footer file

class Footer extends Component {
  render() {
    return (
      <div className="text-center" >
        <div style={{backgroundColor: '#003366', borderTop: "4px solid #fcba19", height: '200px' }}>
            <img 
            src="https://www2.gov.bc.ca/StaticWebResources/static/gov3/images/gov_bc_logo.svg"
            width="200"
            className="img-thumbnail"
            style={{ marginTop: "80px", backgroundColor: '#003366', border: "none"}}
            />
        </div>
      </div>
    );
  }
}

export default Footer;