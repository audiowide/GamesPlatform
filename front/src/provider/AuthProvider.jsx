import {useState, createContext} from 'react'


export const AuthContext = createContext()

const AuthProvider = ({children}) => {

    const [isAuth, setIsAuth] = useState(localStorage.getItem('token')? true : false)
    const [name, setName] = useState(localStorage.getItem('name')? localStorage.getItem('name'): '')
    
  return (
    <AuthContext.Provider value={{isAuth, setIsAuth, name, setName}} >
        {children}
    </AuthContext.Provider>
  )
}

export default AuthProvider
