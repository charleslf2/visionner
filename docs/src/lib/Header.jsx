import React from 'react'
import styles from "../styles/Header.module.css"
import {FaCopy, FaExternalLinkAlt} from 'react-icons/fa'
import {CopyToClipboard} from 'react-copy-to-clipboard';

const Header = () => {
  return (
    <div className={styles.container}>
        
        <div className={styles.logo}> 
            <h1> Visionner</h1> <span>v0.0.4-alpha</span>        
        </div>

        <div className={styles.slogan}>
            <p>Your Image dataset toolkit 😍 </p>
        </div>

        <div className={styles.CTA}>

              <div className={styles.install}>

                <p>pip install visionner</p>
                <CopyToClipboard text="pip install visionner">
                  <button><FaCopy size={20}/></button>
                </CopyToClipboard>

              </div>


              <a  href='https://github.com/charleslf2/Visionner'target="_blank"
               className={styles.github}>
                Github
                <FaExternalLinkAlt/>
              </a>
             
        </div>
    </div>
  )
}

export default Header