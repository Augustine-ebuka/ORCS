import "../styles/register.css";
import Button from "../components/button";
import InputForm from "../components/input";
import Layout from "../components/layout";
import { useState } from "react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function Register() {
  const faculty = ['SOS', 'SOC', 'PLD'];
  const department = ['SEN', 'CSC', 'IFT'];
  const level = ['100', '200', '300', '400', '500'];
  const api = '';

  const [formData, setFormdata] = useState({
    first_name: '',
    middle_name: '',
    last_name: '',
    faculty: '',
    department: '',
    image: '',
    matric_no: '',
    level: '',
    password: ''
  });

  const formSubmit = (event: any) => {
    event.preventDefault();
    // Perform validation
    if (!validateForm()) {
      return;
    }
    // Submit the form data to the API
    // ...
  };

  const handleSubmit = (event: any) => {
    const { name, value } = event.target;
    setFormdata((prevData) => ({ ...prevData, [name]: value }));
  };

  const validateForm = () => {
    if (
      formData.first_name.trim() === '' ||
      formData.last_name.trim() === '' ||
      formData.faculty.trim() === '' ||
      formData.department.trim() === '' ||
      formData.matric_no.trim() === '' ||
      formData.level.trim() === '' ||
      formData.password.trim() === ''
    ) {
      toast.error('Please fill in all required fields');
      return false;
    }
    return true;
  };

  return (
    <>
      <Layout leftmargin={150} rightmargin={150}>
        <ToastContainer />
        <form onSubmit={formSubmit}>
          <div className="register_container">
            <h1>Student details registration</h1>
            <div className="three_col">
              <InputForm
                inputName="first_name"
                inputType="text"
                placeholder="first name"
                label="first name"
                value={formData.first_name}
                onChange={handleSubmit}
              />
              <InputForm
                inputName="middle_name"
                inputType="text"
                placeholder="middle name"
                label="middle name"
                onChange={handleSubmit}
              />
              <InputForm
                inputName="last_name"
                inputType="text"
                placeholder="last name"
                label="last name"
                onChange={handleSubmit}
              />
            </div>
            <div className="two_col">
              <InputForm
                inputName="matric_no"
                inputType="text"
                placeholder="matric number"
                label="matric No"
                onChange={handleSubmit}
              />
              <InputForm
                inputName="password"
                inputType="password"
                placeholder="password"
                label="password"
                onChange={handleSubmit}
              />
            </div>
            <div className="two_col">
              <InputForm
                inputName="faculty"
                inputType="select"
                placeholder="Faculty"
                options={faculty}
                label="faculty"
                onChange={handleSubmit}
              />
              <InputForm
                inputName="department"
                inputType="select"
                placeholder="department"
                options={department}
                label="department"
                onChange={handleSubmit}
              />
            </div>
            <div className="two_col">
              <InputForm
                inputName="image"
                inputType="file"
                placeholder="image"
                label="image"
                onChange={handleSubmit}
              />
              <InputForm
                inputName="level"
                inputType="select"
                placeholder="level"
                options={level}
                label="level"
                onChange={handleSubmit}
              />
            </div>
            <Button buttonName="submit details"/>
          </div>
        </form>
      </Layout>
    </>
  );
}

export default Register;