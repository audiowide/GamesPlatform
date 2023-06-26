import React, { useEffect } from 'react'
import styles from './Auth.module.css'

const SignOut = () => {

  useEffect(() => {
    document.title = 'Sign Out'
  }, [])

  return (
    <div>
       <h2>Sign Out</h2>
      <form action="" className={styles.form}>
        <p>You have been successfully signed out</p>
      </form>
    </div>
  )
}

export default SignOut
