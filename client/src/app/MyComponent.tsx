import axios from 'axios';
import { useEffect, useState } from 'react';

interface Product {
    name: string;
    price: number;
}

function MyComponent() {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/products/');
                setProducts(response.data.products);
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            {products.map((product, index) => (
                <div key={index}>
                    <h3>{product.name}</h3>
                    <p>{product.price}</p>
                </div>
            ))}
        </div>
    );
}

export default MyComponent;