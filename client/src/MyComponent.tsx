import axios from 'axios';
import { useEffect, useState } from 'react';

interface Product {
  name: string;
  price: number;
  description: string;
  thumbnail: string;
}

function Base() {
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
          <p>{product.description}</p>
          <img src={product.thumbnail} alt="" rel={product.name} />
        </div>
      ))}
    </div>
  );
}

export default Base;
