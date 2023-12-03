
import {Routes, Route}  from 'react-router-dom'
import Login from './pages/login'
import Register from './pages/register'
import Dashboard from './pages/dashboard'

function App() {


  return (
    <>
      <Routes>
        <Route path='/' element={<Login />} />
        <Route path='/register' element={<Register />} />
        <Route path='/student/dashboard' element={<Dashboard />} />
      </Routes>
    </>
  )
}

export default App
