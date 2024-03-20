import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

const BookList = () => {
    // Hard coded example
    // const books = [
    //     {'title': 'Book 1', author: {'name': 'Penka'}},
    //     {'title': 'Book 2', author: {'name': 'Obshtata'}},
    //     {'title': 'Book 3', author: {'name': 'Ivan'}},
    //     {'title': 'Book 4', author: {'name': 'Stoyan'}},
    // ]

    const [books, setBooks] = useState([])

    useEffect(() => {

        fetch('http://localhost:8000/books/')
            .then(response => response.json())
            .then(books => setBooks(books));
    }, []);

    return (
        <ul>
            {books.map(book => (
                <li><strong>{book.title}</strong> by <strong>{book.author.name}</strong></li>
            ))}
        </ul>
    );
};

const Loader = () => {
    return (
        <div>
            <img src={logo} alt=""/>
        </div>
    )
};

const App = () => {
    return (
        <div className="App">
            <Loader/>
            <BookList/>
        </div>
    );
}

export default App;
