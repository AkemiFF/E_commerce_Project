import React from 'react'
import ReactDOM from 'react-dom/client'
import Base from './templates/productList.tsx';
import Header from './templates/header.tsx';
import './static/css/index.css'

let head = document.getElementById('header')!;
let container = document.getElementById('root')!;

ReactDOM.createRoot(container).render(
  <React.StrictMode>
    <Base />
  </React.StrictMode>,
)
ReactDOM.hydrateRoot(head, <Header />)