import React, { useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, BarChart, Bar, ComposedChart, Legend, Brush, Area, Label, ScatterChart, Scatter, Cell } from 'recharts';



const width = window.innerWidth;
const height = window.innerHeight;
const Dashboard = () => {
  const generateRandomData = () => {
    return Array.from({ length: 7 }, (_, i) => ({
      name: `Page ${String.fromCharCode(65 + i)}`, // 'Page A', 'Page B', etc.
      uv: Math.floor(Math.random() * 1000), // random number between 0 and 1000
      pv: Math.floor(Math.random() * 1000), // random number between 0 and 1000
      amt: Math.floor(Math.random() * 1000), // random number between 0 and 1000
    }));
  };
  const [data, setData] = useState(generateRandomData());
  const [barData, setBarData] = useState(generateRandomData());
  const [dashData, setDashData] = useState(generateRandomData());
  const [composedData, setComposedData] = useState(generateRandomData());
  const [coaxialData, setCoaxialData] = useState(generateRandomData());
  const [brushBarData, setBrushBarData] = useState(generateRandomData());
  const [scatterData, setScatterData] = useState(generateRandomData());
  const [scatterCellData, setScatterCellData] = useState(generateRandomData());
  const [selectedChart, setSelectedChart] = useState('LineChart');
  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];
  const renderChart = () => {

    switch (selectedChart) {
      case 'LineChart':
        return (<>
          <LineChart width={500} height={300} data={data}>
            <Line type="monotone" dataKey="uv" stroke="#8884d8" />
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
          </LineChart>
          <LineChart width={500} height={300} data={dashData}>
            <Line type="monotone" dataKey="uv" stroke="#8884d8" strokeDasharray="5 5" />
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
          </LineChart>
          <LineChart width={500} height={300} data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis yAxisId="left" />
            <YAxis yAxisId="right" orientation="right" />
            <Tooltip />
            <Line yAxisId="left" type="monotone" dataKey="uv" stroke="#8884d8" />
            <Line yAxisId="right" type="monotone" dataKey="pv" stroke="#82ca9d" />
          </LineChart>
        </>
        );
      case 'BarChart':
        return (<>
          <BarChart width={500} height={300} data={barData}>
            <Bar dataKey='uv' fill='#8884d8' />
          </BarChart>
          <BarChart width={600} height={300} data={brushBarData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="uv" fill="#8884d8" />
            <Brush dataKey="name" height={30} stroke="#8884d8" />
          </BarChart></>
        );
      case 'ComposedChart':
        return (<>
          <ComposedChart width={500} height={400} data={composedData}>
            <CartesianGrid stroke="#f5f5f5" />
            <XAxis dataKey="name" scale="band" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Area type="monotone" dataKey="amt" fill="#8884d8" stroke="#8884d8" />
            <Bar dataKey="pv" barSize={20} fill="#413ea0" />
            <Line type="monotone" dataKey="uv" stroke="#ff7300" />
          </ComposedChart>
          <ComposedChart width={500} height={400} data={coaxialData}>
            <CartesianGrid stroke="#f5f5f5" />
            <XAxis dataKey="name">
              <Label value="Pages" position="insideBottomRight" offset={0} />
            </XAxis>
            <YAxis>
              <Label angle={-90} value="uv" position="insideLeft" style={{ textAnchor: 'middle' }} />
            </YAxis>
            <Tooltip />
            <Legend />
            <Bar dataKey="uv" barSize={20} fill="#413ea0" />
            <Line type="monotone" dataKey="uv" stroke="#ff7300" />
            <Area type="monotone" dataKey="amt" fill="#8884d8" stroke="#8884d8" />
          </ComposedChart>
        </>
        );
      case 'ScatterChart': return (<>
        <ScatterChart width={500} height={300} >
          <CartesianGrid />
          <XAxis dataKey={"uv"} name='uv' unit='k' />
          <YAxis dataKey={"pv"} name='pv' unit='k' />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} />
          <Scatter name='A school' data={scatterCellData} fill='#8884d8' />
        </ScatterChart>
        <ScatterChart width={500} height={300} >
          <CartesianGrid />
          <XAxis dataKey={"uv"} name='uv' unit='k' />
          <YAxis dataKey={"pv"} name='pv' unit='k' />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} />
          <Scatter name='A school' data={scatterData}>
            {
              scatterData.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
            }
          </Scatter>
        </ScatterChart></>)
      default:
        return null;
    }
  };
  return (<View style={styles.container}>
    <Text style={styles.header}>Dashboard Header</Text>
    <View style={styles.content}>
      <View style={styles.sidebar}>
        <TouchableOpacity style={styles.menuItem} onPress={() => setSelectedChart('LineChart')}>
          <Text>Line Charts</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menuItem} onPress={() => setSelectedChart('BarChart')}>
          <Text>Bar Charts</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menuItem} onPress={() => setSelectedChart('ComposedChart')}>
          <Text>Composed Charts</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menuItem} onPress={() => setSelectedChart('ScatterChart')}>
          <Text>Scatter Charts</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.main}>
        {renderChart()}
      </View>
    </View>
    <Text style={styles.footer}>Dashboard Footer</Text>
  </View>)

};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#F5F5F5',
    padding: 20,
  },
  header: {
    fontSize: width * 0.05,
    fontWeight: '600',
    color: '#333',
    marginBottom: 20,
  },
  content: {
    flex: 1,
    flexDirection: 'column',
  },
  sidebar: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 15,

    backgroundColor: '#fff',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  menuItem: {
    padding: 10,
    backgroundColor: '#f5f5f5',
    borderRadius: 5,
  },
  main: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'center',
    padding: 20,

  },
  footer: {
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default {
  title: "dashboard",
  navigator: Dashboard
};
