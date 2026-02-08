import { useState } from 'react';
import { Alert, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function HomeScreen() {
  // 👇 YOUR PERMANENT CLOUD URL
  const API_URL = 'https://brain-api-1ezi.onrender.com';

  const [status, setStatus] = useState('READY');

  const sendSignal = async () => {
    setStatus('SENDING...');
    console.log(`Attempting to hit: ${API_URL}/activate`); // Debug log

    try {
      // 👇 use backticks ` ` here, not single quotes ' '
      const response = await fetch(`${API_URL}/activate`);

      // 1. Check if the Server is happy (Status 200-299)
      if (!response.ok) {
        throw new Error(`Server Error: ${response.status}`);
      }

      // 2. Only parse JSON if the server is happy
      const data = await response.json();
      
      setStatus('RECEIVED!');
      Alert.alert('Brain Response', JSON.stringify(data)); // Show exact response

    } catch (error: any) {
      setStatus('ERROR');
      // 👇 This will now tell us exactly WHAT went wrong
      Alert.alert('Failure', error.message);
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Neural Controller</Text>
      <Text style={styles.status}>STATUS: {status}</Text>

      <TouchableOpacity 
        style={styles.button}
        onPress={sendSignal}
      >
        <Text style={styles.buttonText}>ACTIVATE</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#1a1a1a', alignItems: 'center', justifyContent: 'center' },
  title: { fontSize: 32, fontWeight: 'bold', color: '#00ffcc', marginBottom: 10 },
  status: { fontSize: 18, color: '#00ff00', marginBottom: 50 },
  button: { backgroundColor: '#ff0055', paddingHorizontal: 40, paddingVertical: 20, borderRadius: 15, borderWidth: 2, borderColor: '#ff99aa' },
  buttonText: { color: 'white', fontSize: 24, fontWeight: 'bold' },
});