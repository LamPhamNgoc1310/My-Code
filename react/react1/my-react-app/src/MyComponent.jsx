import React, {useState} from 'react';

function MyComponent () {
    const [name, setName] = useState("Lam");

    const updateName = () => {
        // name = "SpongBob"
        setName("SpongeBob");
    }
    return(
        <div>
            <p>Name: {name}</p>
            <button onClick={updateName}>Set Name</button>
        </div>
    )
}
export default MyComponent