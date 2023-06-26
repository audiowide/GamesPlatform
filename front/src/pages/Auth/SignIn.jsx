import { useEffect, useState } from 'react'
import { $axios } from '../../api'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../../hooks/useAuth'
import styles from './Auth.module.css'
import Button from './../../components/ui/Button/Button'

const SignIn = () => {
  // states
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate('')
  const {setIsAuth, setName} = useAuth()
  const [error, setError] = useState('')

  // useEffect
  useEffect(() => {
    document.title = 'Sign In'
  }, [])

  // auth model
  const auth = (e) => {
    e.preventDefault()
    console.log(email, password)

    $axios.post('/auth/sign-in', 
    { email: email, 
      password: password }).then(res => {
        console.log(res.data)

        setIsAuth(true)
        localStorage.setItem('token', res.data.token)

        setName(email)
        localStorage.setItem('name', email)

        navigate('/')
      }) 
      .catch(err => {
        console.log(err)
        setError(err.response.data.message)
      })
  }

  return (
    <div className='page'> 
      <h2>Sign In</h2>
      <form action="" className={styles.form}>
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
          <Button onClick={auth}>Sign Ip</Button>
          <a href="/" className='link'>Cancel</a>
        </div>
      </form>
    </div>
  )
}

export default SignIn
