import { useEffect, useState } from 'react'
import Button from '../../components/ui/Button/Button'
import { useAuth } from '../../hooks/useAuth'
import { useNavigate } from 'react-router-dom'
import { $axios } from '../../api'
import styles from './Auth.module.css'


const SignUp = () => {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const navigate = useNavigate('')
  const {setIsAuth, setName} = useAuth()


  useEffect(() => {
    document.title = 'Sign Up'
  }, [])

  const auth = (e) => {
    e.preventDefault()
    console.log(email, password)

    $axios.post('auth/sign-up', 
    { username: username,
      email: email, 
      password: password }).then(res => {
        console.log(res.data)

        setIsAuth(true)
        localStorage.setItem('token', res.data.token)

        setName(email)
        localStorage.setItem('name', email)

        navigate('/')
      }).catch(err => {
        console.log(err)
        setError(err.response.data)
      })
  }

  return (
    <div className='page'> 
      <h2>Sign Up</h2>
      <form action="" className={styles.form}>
      <input 
          type="text"
          value={username}
          onChange={e => setUsername(e.target.value)}
          placeholder='Username'
          required
        />
        <input 
          type="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder='Email'
          required
        />
        <input 
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder='Password'
          required
        />
        {error && <p className='error'>{error}</p>}
        <div className="buttons">
          <Button onClick={auth}>Sign Up</Button>
          <a href="/" className='link'>Cancel</a>
        </div>
      </form>
    </div>
  )
}

export default SignUp
