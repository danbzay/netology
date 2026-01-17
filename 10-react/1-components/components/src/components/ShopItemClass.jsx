import React, { Component } from 'react';

export default class ShopItemClass extends Component {
  constructor(props) {
    super(props);
    //this.item = props;
    console.log('props=' + JSON.stringify(props));
    //this.state = { count: 0 };
  }

  render() {
    const item = this.props.item;
    return (
      <div className="main-content">
        <h2>{item.brand}</h2>
        <h1>{item.title}</h1>
        <h3>{item.description}</h3>
        <div className="description">{item.descriptionFull}</div>
        <div className="highlight-window mobile"><div className="highlight-overlay">
        </div></div>
        <div className="divider"></div>
        <div className="purchase-info">
          <p className="price">{item.currency}{item.price.toFixed(2)}</p>
          <button>Добавить в корзину</button>
        </div>
      </div>
    )
  }
}


