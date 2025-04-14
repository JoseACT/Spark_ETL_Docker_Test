-- UUID extension
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create the final storage table
CREATE TABLE IF NOT EXISTS _stage (
    transactionId               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clientId        INTEGER NOT NULL,
    sourceId        INTEGER NOT NULL,
    oldId           TEXT NOT NULL,
    value            DOUBLE PRECISION,
    createdAt       TIMESTAMP WITH TIME ZONE,
    typeTransaction INTEGER,
    processedAt     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    batchId         TEXT NOT NULL DEFAULT '0'
);
