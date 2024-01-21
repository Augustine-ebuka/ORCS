import '../styles/result.css'
// import Button from './button'
// import CourseTable from './table'
import httpClient from './httpClient';
import { useEffect, useState } from 'react';
import '../styles/res.css'
function Result() {
  const [criteria, setCrateria] = useState({
    "session":'',
    "semester":''
  })
  const [seeresult, setResult] = useState([])
useEffect(()=>{
  fetchResult
},[])
const [alert, setAlert] = useState('')

  const fetchResult = async()=>{
    try {
      const endpoint = 'http://localhost:5000/api/result'

      const result = await httpClient.get(endpoint,{ params: criteria })
      setAlert('loading')

      if (result.status === 200) {
        setResult(result.data.result)
        console.log(seeresult)
        console.log(result.data.result)
        setAlert('')
        
      } else if(result.status === 404) {
        setAlert('data not found')
        console.log('data not found');
      }
    } catch (error:any) {
      console.error('Error fetching result:', error.message);
      
    }finally{
      setAlert('done regardles')
    }
  }


  const handleOnChange = (event:any) => {
    const { name, value } = event.target;
    setCrateria((prev) => ({ ...prev, [name]: value }));
  };
  console.log(criteria);
  
  

    return (
        <>
            <div className="result-container">
                <div className="result-header">
                    <div className="input-form">
                    <label htmlFor="session">session</label>
          
                    <select name="session" value={criteria.session} defaultValue="2022/2023" onChange={handleOnChange}>
                        <option value="2022/2023">2022/2023</option>
                        <option value="2022/2023">2022/2023</option>
                    </select>
                    </div>
                    <div className="input-form">
                    <label htmlFor="semester">Semester</label>

                    <select name="semester" value={criteria.semester} defaultValue='first' onChange={handleOnChange}>
                        <option value="first">1st semsetr</option>
                        <option value="second">2nd semester</option>
                    </select>

                    </div>
                    <div className="input-form">
                    <label htmlFor="level">Level</label>

                    <select name="level" value='level'>
                        <option value="session">100</option>
                        <option value="session">200</option>
                        <option value="session">300</option>
                        <option value="session">400</option>
                        <option value="session">500</option>
                    </select>
                    
                    </div>
                    <button onClick={fetchResult} className='checkresultbtn'>submit</button>
                  
                </div>
                    
                  <div className="resul-table">
                  <table>
                    <thead>
                      <tr>
                        <th>Course Code</th>
                        <th>Course Unit</th>
                        <th>Mark</th>
                        <th>Grade Point</th>
                        <th>Session</th>
                        <th>Semester</th>
                      </tr>
                    </thead>
                    <tbody>
                      {seeresult?.map((result:any, index) => (
                        <tr key={index}>
                          <td>{result.course_code}</td>
                          <td>{result.course_unit}</td>
                          <td>{result.mark}</td>
                          <td>{result.grade}</td>
                          <td>{result.session}</td>
                          <td>{result.semester}</td>
                        </tr>
                        
                       
                      ))}
                      {alert}
                    </tbody>
                  </table>
                </div>
                </div>
        </>
    )
}
export default Result
