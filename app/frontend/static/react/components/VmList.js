import React, { useEffect, useState } from 'react';
import './VmList.css'; 
const VmList = () => {
    const [vms, setVMs] = useState([]);
    useEffect(() => {
        fetch('/api/vms/')
            .then(response => response.json())
            .then(data => setVMs(data))
            .catch(error => console.error('Error fetching VMs:', error));
    }, []);
    return (
        <div>
            <h1>VMs</h1>
            <table>
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Ssh Key</th>
                        <th>CPUs</th>
                        <th>RAM</th>
                        <th>Server</th>
                        <th>Active</th>
                    </tr>
                </thead>
                <tbody>
                    {vms.map((vm, index) => (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>{vm.ssh_key || 'N/A'}</td>
                            <td>{vm.cpus}</td>
                            <td>{vm.ram}</td>
                            <td>{vm?.server?.region ||'N/A' }</td>
                            <td>{vm.active.toString()}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default VmList;
