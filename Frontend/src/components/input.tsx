import {FC} from 'react'
import '../styles/input.css'
interface InputProps{
    label? : string,
    inputName : string
    placeholder? : string
    inputType: (string|number|any)
}
const InputForm : FC<InputProps> = ({
    label,
    inputName,
    inputType,
    placeholder
}) =>{

    return (
        <>
        <div className='input-form'>
        <label htmlFor={label}> {label}</label>
        <input 
        name={inputName} 
        type={inputType} 
        placeholder={placeholder}
        >    
        </input>
        </div>    
        </>
    )
}
export default InputForm
