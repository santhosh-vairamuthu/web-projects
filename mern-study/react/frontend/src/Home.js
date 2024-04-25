import React from 'react'

const Home = () => {
    return (
        <div className='container'>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container">
                    <p className="navbar-brand">Apple</p>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                        <p class="nav-link active" aria-current="page">Home</p>
                        </li>
                        <li class="nav-item">
                        <p class="nav-link" >Products</p>
                        </li>
                        <li class="nav-item">
                        <p class="nav-link">About</p>
                        </li>
                        <li class="nav-item">
                        <p class="nav-link">Contact</p>
                        </li>
                    </ul>
                    </div>
                </div>
                </nav>

                <section class="hero bg-dark text-light py-5">
                    <div class="container text-center">
                        <h1 class="display-4">Welcome to Apple</h1>
                        <p class="lead">Explore the latest products and innovations from Apple.</p>
                        <p  class="btn btn-primary btn-lg">Shop Now</p>
                    </div>
                </section>

                <section class="featured-products py-5">
                    <div class="container">
                        <h2 class="text-center mb-4">Featured Products</h2>
                        <div class="row">
                            <div class="col-md-4 mb-4">
                                <div class="card">
                                    <img src="https://via.placeholder.com/300" class="card-img-top" alt="Product1"/>
                                    <div class="card-body">
                                        <h5 class="card-title">iPhone 13 Pro</h5>
                                        <p class="card-text">$999</p>
                                        <p  class="btn btn-primary">View Details</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 mb-4">
                                <div class="card">
                                    <img src="https://via.placeholder.com/300" class="card-img-top" alt="Product2"/>
                                    <div class="card-body">
                                        <h5 class="card-title">MacBook Pro</h5>
                                        <p class="card-text">$1299</p>
                                        <p  class="btn btn-primary">View Details</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 mb-4">
                                <div class="card">
                                    <img src="https://via.placeholder.com/300" class="card-img-top" alt="Product3"/>
                                    <div class="card-body">
                                        <h5 class="card-title">AirPods Pro</h5>
                                        <p class="card-text">$249</p>
                                        <p  class="btn btn-primary">View Details</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <footer class="bg-dark text-light py-4">
                    <div class="container text-center">
                        <p>&copy; 2024 Apple Inc. All rights reserved.</p>
                    </div>
                </footer>

        </div>
    );
}

export default Home