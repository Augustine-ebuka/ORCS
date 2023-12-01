import {FC} from 'react'
import '../styles/button.css';

interface ButtonProp{
    onClick?: string,
    buttonName: string
}

const Button : FC<ButtonProp>= ({ onClick, buttonName }) => {
  return (
    <button className="button" type="submit" >
      {buttonName}
    </button>
  );
};

export default Button;