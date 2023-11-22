import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
// STEP: Import these 2 below
import { RouterProvider } from 'react-router-dom'
import router from './router.jsx'
//supposed to import boostrap here? istead of linking in index.html like I did

ReactDOM.createRoot(document.getElementById('root')).render(
  //passes router function as a PROP
    <RouterProvider router={router} />
)
