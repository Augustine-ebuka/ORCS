import { ReactNode, FC } from "react"
import '../styles/header.css'

interface Children{
    children?: ReactNode
}

const Header:FC<Children> = ({children}) =>{
    

    return (
        <>
            <div className="header-container">
                <div className="header-left">
                    <span>SEN/17/2506</span>
                </div>
                <div className="header-right">
                    <span>obetta Augustine.E</span>
                    <span className="pic"></span>
                    <span>logout</span>
                </div>
                {children}
            </div>
        </>
    )
}

export default  Header

