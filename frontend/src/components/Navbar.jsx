import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <nav>
      <Link to="/dashboard">Dashboard</Link> |{' '}
      <Link to="/workflows">Workflows</Link> |{' '}
      <Link to="/editor">Editor</Link> | <Link to="/runs">Runs</Link>
    </nav>
  )
}

export default Navbar
