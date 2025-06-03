'use client'

import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabaseClient'

export default function TestPage() {
  const [status, setStatus] = useState<'loading' | 'success' | 'error'>('loading')
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    async function testSupabase() {
      try {
        // Try to get the current session
        const { data: { session }, error } = await supabase.auth.getSession()
        
        if (error) {
          throw error
        }

        setStatus('success')
      } catch (err) {
        setStatus('error')
        setError(err instanceof Error ? err.message : 'Unknown error occurred')
      }
    }

    testSupabase()
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Supabase Client Test</h1>
      <div className="p-4 border rounded">
        <p>Status: {status}</p>
        {error && <p className="text-red-500">Error: {error}</p>}
        {status === 'success' && (
          <p className="text-green-500">Supabase client initialized successfully!</p>
        )}
      </div>
    </div>
  )
} 