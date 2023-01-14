import React from 'react'
import styles from "../styles/Layout.module.css"
import Showcase_card from './Showcase_card'

const Layout = () => {
  return (
    <div className={styles.wrapper}>
        
        <div className={styles.container}>

            <div className={styles.title}>What visionner can do for you ?</div>

            <div className={styles.showcase_container}>

                <div className={styles.showcase_01}>
                    <Showcase_card/>

                </div>

                <div className={styles.showcase_02}>
                    
                </div>

                <div className={styles.showcase_03}>
                    
                </div>

            </div>
        </div>
    </div>

    
  )
}

export default Layout