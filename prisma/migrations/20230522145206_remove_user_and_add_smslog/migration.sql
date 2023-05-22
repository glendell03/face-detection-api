/*
  Warnings:

  - You are about to drop the `User` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `UserData` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "UserData" DROP CONSTRAINT "UserData_userId_fkey";

-- DropTable
DROP TABLE "User";

-- DropTable
DROP TABLE "UserData";

-- CreateTable
CREATE TABLE "SmsLog" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "photo" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "SmsLog_pkey" PRIMARY KEY ("id")
);
