import React from 'react';
import '../styles/input.css';

interface InputProps {
  label?: string;
  inputName: string;
  placeholder?: string;
  inputType: string | number | any;
  options?: string[];
  onChange?: (event:any)=> any
  value?: any
}

const InputForm: React.FC<InputProps> = ({
  label,
  inputName,
  inputType,
  placeholder,
  options,
  onChange,
  value
}) => {
  return (
    <div className="input-form">
      <label htmlFor={inputName}>{label}</label>
      {inputType === 'select' ? (
        <select name={inputName} value={value} onChange={onChange}>
          {options &&
            options.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
        </select>
      ) : (
        <input
          name={inputName}
          type={inputType}
          placeholder={placeholder}
          onChange={onChange}
          value = {value}
        />
      )}
    </div>
  );
};

export default InputForm;