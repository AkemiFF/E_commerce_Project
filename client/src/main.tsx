import React from 'react'
import ReactDOM from 'react-dom/client'
import Base from './MyComponent.tsx'
import './index.css'

let container = document.getElementById('root')!;

ReactDOM.createRoot(container).render(
  <React.StrictMode>
    <Base />
  </React.StrictMode>,
)
