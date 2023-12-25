
import {Routes, Route}  from 'react-router-dom'
import Login from './pages/login'
import Register from './pages/register'
import Dashboard from './pages/dashboard'
import Sidebar from './components/sidebar'
function App() {


  return (
    <>
    <Sidebar>
      <Routes>
        <Route path='/' element={<Login />} />
        <Route path='/register' element={<Register />} />
        <Route path='/student/dashboard' element={<Dashboard />} />
      </Routes>
    </Sidebar>
    </>
  )
}

export default App
