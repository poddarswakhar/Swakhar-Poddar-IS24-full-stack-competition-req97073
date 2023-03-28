import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Home from "./components/Home";
import Footer from "./components/Footer";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Home />
        <br></br><br></br>
        <Footer />
      </Fragment>
    );
  }
}

export default App;