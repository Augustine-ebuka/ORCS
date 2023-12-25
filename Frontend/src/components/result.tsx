import '../styles/result.css'
import Button from './button'
import CourseTable from './table'
function Result() {
    const courses = [
        {
          code: 'CSE101',
          title: 'Introduction to Computer Science',
          credit: 3,
          grade: 'A',
          gradePoint: 4.0,
        },
        {
          code: 'CSE101',
          title: 'Introduction to Computer Science',
          credit: 3,
          grade: 'A',
          gradePoint: 4.0,
        },
        {
          code: 'CSE101',
          title: 'Introduction to Computer Science',
          credit: 3,
          grade: 'A',
          gradePoint: 4.0,
        },
        {
          code: 'CSE101',
          title: 'Introduction to Computer Science',
          credit: 3,
          grade: 'A',
          gradePoint: 4.0,
        },
        {
          code: 'CSE101',
          title: 'Introduction to Computer Science',
          credit: 3,
          grade: 'A',
          gradePoint: 4.0,
        },
        // Add more courses here...
      ];

    return (
        <>
            <div className="result-container">
                <div className="result-header">
                    <div className="input-form">
                    <label htmlFor="session">session</label>
                    <select name="session" value='session'>
                        <option value="session">2021/2022</option>
                        <option value="session">2021/2022</option>
                        <option value="session">2021/2022</option>
                        <option value="session">2021/2022</option>
                        <option value="session">2021/2022</option>
                    </select>
                    </div>
                    <div className="input-form">
                    <label htmlFor="semester">Semester</label>
                    <select name="semester" value='semester'>
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
                    <Button buttonName='submit'></Button>
                </div>
                <div className="resul-table">
                    <CourseTable courses={courses}>

                    </CourseTable>
                </div>

            </div>
        </>
    )
}
export default Result
