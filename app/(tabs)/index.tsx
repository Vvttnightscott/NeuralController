import { useState } from 'react';
import { Alert, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function HomeScreen() {
// 👇 YOUR PERMANENT CLOUD URL (No more ngrok!)
const API_URL = 'https://brain-api-1ezi.onrender.com';
// (Make sure to use YOUR actual URL from the Render dashboard); 
  
  const [status, setStatus] = useState('READY');

  const sendSignal = async () => {
    setStatus('SENDING...');
    try {
      const response = await fetch(`${API_URL}/activate`);
      const data = await response.json();
      
      // If success:
      setStatus('RECEIVED!');
      Alert.alert('Brain Response', data.message); // Should say "Command Executed"
      
    } catch (error) {
      setStatus('ERROR');
      Alert.alert('Connection Failed', 'Could not find the Brain. Check IP or Firewall.');
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