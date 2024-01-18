import { FC } from "react"
import '../styles/header.css'
import httpClient from "./httpClient"
import { useNavigate } from "react-router-dom"

interface studentDetails{
    department?:string,
    faculty?:string,
    first_name?:string,
    matric_no?:string,
    level?:string
}

const Header:FC<studentDetails> = ({first_name, department, faculty,matric_no, level}) =>{
    const navigate = useNavigate()
    const logout = async()=>{
        const api = 'http://localhost:5000/api/student/logout'
        try {
            const result = await httpClient.post(api)
            if (result.status === 200) {
                console.log("success")
                navigate('/')

            }
        } catch (error) {
            console.log(error)
        }

    }
    

    return (
        <>
            <div className="header-container">
                <div className="header-left">
                    <span>welcome {matric_no}!</span>
                </div>
                <div className="header-right">
                    <span>{first_name}</span>
                    <span className="pic"></span>
                    <button className="logout" onClick={logout}>logout</button>
                </div>
            </div>
        </>
    )
}

export default  Header

