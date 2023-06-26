import { useNavigate } from 'react-router-dom'
import { useAuth } from '../../hooks/useAuth'
import styles from './Header.module.css'

const Header = () => {
  const {isAuth, setIsAuth, setName, name} = useAuth()
  const navigate = useNavigate()


  const logout = (e) => {
    e.preventDefault()

    setIsAuth(false)
    setName('')

    localStorage.clear()
    
    navigate('/sign-out')
  }

  return (
    <div className={styles.header}> 
        <a href='/' className={styles.header__logo}>WorldSkills: Games</a>
        <div className={styles.header__right}>
            {isAuth? (
              <>
                <a className="link">{name}</a>
              <a onClick={logout} className="link">logout</a>
              </>
            ): (
              <>
                <a href="/sign-up" className="link">Sign Up</a>
              <a href="/sign-in" className="link">Sign In</a>
              </>
            )}
        </div>
    </div>
  )
}

export default Header
