import { Route, Routes } from 'react-router-dom'
import Home from './pages/Home/Home'
import SignUp from './pages/Auth/SignUp'
import SignIn from './pages/Auth/SignIn'
import SignOut from './pages/Auth/SignOut'
import Header from './components/header/Header'
import { useAuth } from './hooks/useAuth'
import User from './pages/User/User'
import NotFound from './pages/NotFound/NotFound'
import ManageGame from './pages/ManageGame/ManageGame'
import Game from './pages/Game/Game'

const Router = () => {
  const {isAuth, setIsAuth, setName, name} = useAuth()

  return (
    <div className='pre__page'>
      <Header/>
      <Routes>
        <Route path='/' element={<Home/>}/>

        <Route path='/sign-up' element={<SignUp/>}/>
        <Route path='/sign-in' element={<SignIn/>}/>
        <Route path='/sign-out' element={<SignOut/>}/>

        <Route path='*' element={<NotFound/>}/>  

        {isAuth && <Route path='/users/:username' element={<User/>} />}
        {isAuth && <Route path='/games/:slug/edit' element={<ManageGame/>} />}    
        {isAuth && <Route path='/games/:slug' element={<Game/>} />}        
      </Routes>
    </div>
  )
}

export default Router
