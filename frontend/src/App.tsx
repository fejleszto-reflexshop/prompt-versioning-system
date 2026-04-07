import { useEffect } from 'react'

function App() {

    useEffect(() => {
      create_acc()
    }, []);

    return (
        <>
          <h4>test</h4>
        </>
    )
}

async function create_acc() {
    const call = await fetch('http://127.0.0.1:5000/new-acc', {
      method: 'POST',
      headers: {},
      body: JSON.stringify({"u": "test", "p": "test password"})
    })

    const response = await call.json().catch(err => console.log(err))

    console.log(response)
}

export default App
