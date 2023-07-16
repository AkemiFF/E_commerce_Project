import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.tsx'
import MyComponent from './MyComponent.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MyComponent />
  </React.StrictMode>,
)
