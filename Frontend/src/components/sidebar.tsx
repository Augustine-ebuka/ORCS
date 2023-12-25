import { useState, createContext, ReactNode } from 'react'
import '../styles/sidebar.css'

interface Children{
    children: ReactNode
}
interface sidebarIndx{
    setActive:(index:any)=>void
    isActive:number | null
}
export const MyContext = createContext<sidebarIndx>({isActive:null, setActive:(index:number) => {}})
function Sidebar({children}: Children) {
    const [isActive , setIsactive] = useState<number | null>(null)

    const setActive = (index:number | null)=>{
        console.log(index);
        setIsactive(index)
    }

    const bundle:sidebarIndx = {
        isActive,
        setActive
}


    return (
        <>
        <MyContext.Provider value={bundle}>
            <div className='sidebar_container'>
            {children}
            </div>
        </MyContext.Provider>

        </>
    )
}
export default Sidebar
           