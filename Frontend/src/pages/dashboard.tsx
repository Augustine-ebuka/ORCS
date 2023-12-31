import '../styles/dashboard.css'
import {useState, useEffect  } from "react"
import axios from "axios";
import { useContext } from 'react'
import { MyContext } from '../components/sidebar'
import Header from '../components/header'
import Result from '../components/result'
// import {utilityContext} from '../context/generalContext'


function Dashboard() {
    const {isActive,setActive} = useContext(MyContext)
    const [userData, setUserdata] = useState<any>(null)
    const api = 'http://localhost:5000/api/student/info'
    console.log(isActive)
    useEffect(() => {
        const fetchUser = async ()=>{
            try {
                const result = await axios(api)
                if (result.status == 200) {
                    console.log(result)
                    setUserdata(result)
                }
            } catch (error:any) {
                console.log(error)   
            }
            fetchUser()
        }
       }, [])

    return (
        <>
        <div className='dashboard'>
            <div className='sidebar'>
                <ul>
                    <li onClick={()=>setActive(null)} className={isActive == null?'active': ''}>Result</li>
                    <li onClick={()=>setActive(0)} className={isActive === 0?'active':''}>Profile</li>
                    <li onClick={()=>setActive(1)} className={isActive === 1?'active':''}>Payment</li>
                    <li onClick={()=>setActive(2)} className={isActive === 2?'active':''}>Learning</li>
                    <li onClick={()=>setActive(3)} className={isActive === 3?'active':''}>Notificatin</li>
                    <li onClick={()=>setActive(4)} className={isActive === 4?'active':''}>Settings</li>
                </ul>
            </div>
            <div className='main'>
                <Header>
                    
                </Header>
                
                   {isActive === null ? (<Result></Result>) : ''}
                   {isActive === 0 ? (<h1>i am zero</h1>) : ''}
                   {isActive === 1 ? (<h1>i am one</h1>) : ''}
                  { isActive === 2 ? (<h1>i am two</h1>) : ''}
                   {isActive === 3 ? (<h1>i am three</h1>) : ''}
                  { isActive === 4 ? (<h1>i am four</h1>) : ''}
                
                <h1>main bar</h1>
            </div>
        </div> 
        </>
    )
}
export default Dashboard
