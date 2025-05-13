import React, { useState, useEffect } from 'react';
import {
  Container,
  Paper,
  Typography,
  Box,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
  Grid,
  Card,
  CardContent,
  CircularProgress,
  Alert
} from '@mui/material';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from 'recharts';
import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

function App() {
  const [symptoms, setSymptoms] = useState({
    conectividad: '',
    velocidad: '',
    acceso_servidor: '',
    señal_wifi: '',
    errores_dns: ''
  });

  const [diagnosis, setDiagnosis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [testCases, setTestCases] = useState([]);

  useEffect(() => {
    // Cargar casos de prueba
    axios.get(`${API_URL}/test-cases`)
      .then(response => setTestCases(response.data))
      .catch(err => setError('Error al cargar casos de prueba'));
  }, []);

  const handleSymptomChange = (event) => {
    const { name, value } = event.target;
    setSymptoms(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleDiagnose = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${API_URL}/diagnose`, symptoms);
      setDiagnosis(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Error al realizar el diagnóstico');
    } finally {
      setLoading(false);
    }
  };

  const loadTestCase = (testCase) => {
    setSymptoms(testCase.sintomas);
  };

  const renderSymptomSelect = (name, label, options) => (
    <FormControl fullWidth margin="normal">
      <InputLabel>{label}</InputLabel>
      <Select
        name={name}
        value={symptoms[name]}
        label={label}
        onChange={handleSymptomChange}
      >
        {options.map(option => (
          <MenuItem key={option} value={option}>
            {option}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );

  const renderDiagnosisResults = () => {
    if (!diagnosis) return null;

    const chartData = Object.entries(diagnosis.diagnostico).map(([cause, data]) => ({
      name: cause.replace('_', ' ').toUpperCase(),
      value: data.valor
    }));

    return (
      <Box mt={4}>
        <Typography variant="h5" gutterBottom>
          Diagnóstico
        </Typography>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Causa Principal
                </Typography>
                <Typography variant="body1">
                  {diagnosis.causa_principal.replace('_', ' ').toUpperCase()}
                </Typography>
                <Typography variant="h6" gutterBottom sx={{ mt: 2 }}>
                  Probabilidad
                </Typography>
                <Typography variant="body1">
                  {Math.round(diagnosis.valor_principal)}%
                </Typography>
                <Typography variant="h6" gutterBottom sx={{ mt: 2 }}>
                  Recomendación
                </Typography>
                <Typography variant="body1">
                  {diagnosis.recomendacion_principal}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="value" fill="#8884d8" />
              </BarChart>
            </ResponsiveContainer>
          </Grid>
        </Grid>
      </Box>
    );
  };

  return (
    <Container maxWidth="lg">
      <Box py={4}>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Sistema Experto de Diagnóstico de Fallas en Red
        </Typography>

        <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
          <Typography variant="h6" gutterBottom>
            Ingrese los Síntomas
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} md={6}>
              {renderSymptomSelect('conectividad', 'Conectividad', ['nula', 'baja', 'media', 'buena'])}
              {renderSymptomSelect('velocidad', 'Velocidad', ['lenta', 'moderada', 'rápida'])}
              {renderSymptomSelect('acceso_servidor', 'Acceso al Servidor', ['inaccesible', 'lento', 'fluido'])}
            </Grid>
            <Grid item xs={12} md={6}>
              {renderSymptomSelect('señal_wifi', 'Señal Wi-Fi', ['débil', 'aceptable', 'fuerte'])}
              {renderSymptomSelect('errores_dns', 'Errores DNS', ['frecuente', 'ocasional', 'nula'])}
            </Grid>
          </Grid>
          <Box mt={2} display="flex" justifyContent="center">
            <Button
              variant="contained"
              color="primary"
              onClick={handleDiagnose}
              disabled={loading || Object.values(symptoms).some(v => !v)}
            >
              {loading ? <CircularProgress size={24} /> : 'Diagnosticar'}
            </Button>
          </Box>
        </Paper>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        {testCases.length > 0 && (
          <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
            <Typography variant="h6" gutterBottom>
              Casos de Prueba
            </Typography>
            <Grid container spacing={2}>
              {testCases.map((testCase, index) => (
                <Grid item xs={12} sm={6} md={4} key={index}>
                  <Card>
                    <CardContent>
                      <Typography variant="h6" gutterBottom>
                        {testCase.nombre}
                      </Typography>
                      <Button
                        variant="outlined"
                        size="small"
                        onClick={() => loadTestCase(testCase)}
                      >
                        Cargar Caso
                      </Button>
                    </CardContent>
                  </Card>
                </Grid>
              ))}
            </Grid>
          </Paper>
        )}

        {renderDiagnosisResults()}
      </Box>
    </Container>
  );
}

export default App; 