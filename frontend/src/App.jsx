import { BrowserRouter, Route, Routes } from 'react-router-dom'

import Navbar from './components/Navbar'
import Dashboard from './pages/Dashboard'
import Workflows from './pages/Workflows'
import CreateWorkflow from './pages/CreateWorkflow'
import Editor from './pages/Editor'
import Runs from './pages/Runs'

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/workflows" element={<Workflows />} />
        <Route path="/workflows/new" element={<CreateWorkflow />} />
        <Route path="/editor" element={<Editor />} />
        <Route path="/runs" element={<Runs />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
