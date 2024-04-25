import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";

const Auth = () => {
    const [loginEmail, setLoginEmail] = useState('');
    const [loginPassword, setLoginPassword] = useState('');
    const [signupName, setSignupName] = useState('');
    const [signupEmail, setSignupEmail] = useState('');
    const [signupPassword, setSignupPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost:2004/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: loginEmail, password: loginPassword })
            });
            const data = await response.json();
            if (data.status === true) {
                navigate("/");
            } else {
                alert('Invalid credentials');
            }
        } catch (error) {
            console.error('Login failed:', error);
            alert('Login failed. Please try again.');
        }
    };

    const handleSignup = async () => {
        try {
            const response = await fetch('http://localhost:2004/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: signupName, email: signupEmail, password: signupPassword })
            });
            const data = await response.json();
            if (data.status === true) {
                navigate("/");
            } else {
                alert('Error in Signup');
            }
        } catch (error) {
            console.error('Signup failed:', error);
            alert('Signup failed. Please try again.');
        }
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-6">
                    <div className="card">
                        <div className="card-header">
                            <ul className="nav nav-tabs card-header-tabs" id="myTab" role="tablist">
                                <li className="nav-item" role="presentation">
                                    <button className="nav-link active" id="login-tab" data-bs-toggle="tab" data-bs-target="#login" type="button" role="tab" aria-controls="login" aria-selected="true">Login</button>
                                </li>
                                <li className="nav-item" role="presentation">
                                    <button className="nav-link" id="signup-tab" data-bs-toggle="tab" data-bs-target="#signup" type="button" role="tab" aria-controls="signup" aria-selected="false">Signup</button>
                                </li>
                            </ul>
                        </div>
                        <div className="card-body">
                            <div className="tab-content" id="myTabContent">
                                <div className="tab-pane fade show active" id="login" role="tabpanel" aria-labelledby="login-tab">
                                    <div className="mb-3">
                                        <label htmlFor="loginEmail" className="form-label">Email address</label>
                                        <input type="email" className="form-control" id="loginEmail" value={loginEmail} onChange={(e) => setLoginEmail(e.target.value)} aria-describedby="emailHelp" />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="loginPassword" className="form-label">Password</label>
                                        <input type="password" className="form-control" id="loginPassword" value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)} />
                                    </div>
                                    <button type="button" onClick={handleLogin} className="btn btn-primary">Login</button>
                                </div>
                                <div className="tab-pane fade" id="signup" role="tabpanel" aria-labelledby="signup-tab">
                                    <div className="mb-3">
                                        <label htmlFor="signupName" className="form-label">Name</label>
                                        <input type="text" className="form-control" id="signupName" value={signupName} onChange={(e) => setSignupName(e.target.value)} aria-describedby="emailHelp" />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="signupEmail" className="form-label">Email address</label>
                                        <input type="email" className="form-control" id="signupEmail" value={signupEmail} onChange={(e) => setSignupEmail(e.target.value)} aria-describedby="emailHelp" />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="signupPassword" className="form-label">Password</label>
                                        <input type="password" className="form-control" id="signupPassword" value={signupPassword} onChange={(e) => setSignupPassword(e.target.value)} />
                                    </div>
                                    <button type="button" onClick={handleSignup} className="btn btn-primary">Signup</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Auth;
