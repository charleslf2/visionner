import React from 'react'
import styles from "../styles/Header.module.css"


const Header = () => {
  return (
    <div className={styles.container}>
        
        <div className={styles.logo}> 
            <h1> Visionner</h1> <span>v0.0.4-alpha</span>        
        </div>

        <div className={styles.slogan}>
            <h2>Your Image dataset toolkit</h2>
        </div>

        <div className={styles.CTA}>
              <div>
                pip install visionner
              </div>


              <div>
                Github
              </div>
        </div>
    </div>
  )
}

export default Header