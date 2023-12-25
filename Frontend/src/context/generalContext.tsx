import { ReactNode, createContext, FC, Children, useState, useEffect  } from "react"
import axios from "axios";


interface Children{
    children: ReactNode
}

interface contextInterface{
    darkMode: boolean;
    setDark: () => void
    
}

export const utilityContext = createContext<contextInterface>({darkMode:true,setDark:()=>{}})

const GeneralContext:FC<Children> = ({children}) =>{
    const api = 'http://localhost:5000/api/student/info'
    const [darkMode, setDarkmode] = useState(true)
    const [userData, setUserdata] = useState<any>(null)

    const setDark = ()=>{
        setDarkmode(!true)
    }

   useEffect(() => {
    const fetchUser = async ()=>{
        try {
            const result = await axios(api)
            if (result.status ==200) {
                console.log(result)
                setUserdata(result)
            }
        } catch (error:any) {
            console.log(error)   
        }
        fetchUser()
    }
   }, [])
   
    
    const values={
        darkMode,
        setDark,
        userData,
        setUserdata
    }

    return (
        <utilityContext.Provider value={values}>
            {children}
        </utilityContext.Provider>
    )
}
export default GeneralContext