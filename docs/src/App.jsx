import React from 'react'
import Header from '../src/lib/Header'
import styles from "../src/App.module.css"


const App = () => {
  return (
    <div className={styles.wrapper}>

      <div className={styles.container}>

        <Header/>

      </div>

    </div>
  )
}

export default App